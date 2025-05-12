import threading
import time
import random
import os
import matplotlib.pyplot as plt  

# ====== SETUP FOLDER ======
os.makedirs('results', exist_ok=True)
os.makedirs('docs', exist_ok=True)

# ====== PARAMETER ======
NUM_ITERATIONS = 100
NUM_THREADS = 2

# ====== VARIABEL GLOBAL ======
memory = {'x': 0}
caches = [{'x': 0, 'valid': True} for _ in range(NUM_THREADS)]
cache_hits = [0] * NUM_THREADS
mem_access = [0] * NUM_THREADS
coherence_msgs = 0
use_coherence = True
lock = threading.Lock()

# ====== THREAD FUNCTION ======
def thread_function(thread_id):
    global memory, caches, cache_hits, mem_access, coherence_msgs

    for _ in range(NUM_ITERATIONS):
        op = random.choice(['read', 'write'])
        with lock:
            if op == 'read':
                if caches[thread_id]['valid']:
                    cache_hits[thread_id] += 1
                else:
                    caches[thread_id]['x'] = memory['x']
                    caches[thread_id]['valid'] = True
                    mem_access[thread_id] += 1
            else:
                val = random.randint(1, 100)
                caches[thread_id]['x'] = val
                caches[thread_id]['valid'] = True
                memory['x'] = val
                mem_access[thread_id] += 1

                if use_coherence:
                    for i in range(NUM_THREADS):
                        if i != thread_id:
                            caches[i]['valid'] = False
                            coherence_msgs += 1
        time.sleep(0.005)

# ====== SIMULASI ======
def run_simulation(with_coherence=True):
    global caches, memory, cache_hits, mem_access, coherence_msgs, use_coherence

    use_coherence = with_coherence
    caches = [{'x': 0, 'valid': True} for _ in range(NUM_THREADS)]
    memory = {'x': 0}
    cache_hits = [0] * NUM_THREADS
    mem_access = [0] * NUM_THREADS
    coherence_msgs = 0

    threads = []
    start_time = time.time()

    for i in range(NUM_THREADS):
        t = threading.Thread(target=thread_function, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    exec_time = time.time() - start_time

    return {
        'cache_hits': cache_hits,
        'mem_access': mem_access,
        'coherence_msgs': coherence_msgs,
        'exec_time': exec_time
    }

# ====== JALANKAN DAN SIMPAN HASIL ======
result_no_coherence = run_simulation(with_coherence=False)
result_with_coherence = run_simulation(with_coherence=True)

# Simpan hasil ke log file
with open('results/log.txt', 'w') as f:
    f.write("=== HASIL SIMULASI TANPA KOHERENSI ===\n")
    f.write(f"Cache Hits     : {result_no_coherence['cache_hits']}\n")
    f.write(f"Akses Memori   : {result_no_coherence['mem_access']}\n")
    f.write(f"Pesan Koherensi: 0\n")
    f.write(f"Waktu Eksekusi : {result_no_coherence['exec_time']:.4f} detik\n\n")

    f.write("=== HASIL SIMULASI DENGAN KOHERENSI ===\n")
    f.write(f"Cache Hits     : {result_with_coherence['cache_hits']}\n")
    f.write(f"Akses Memori   : {result_with_coherence['mem_access']}\n")
    f.write(f"Pesan Koherensi: {result_with_coherence['coherence_msgs']}\n")
    f.write(f"Waktu Eksekusi : {result_with_coherence['exec_time']:.4f} detik\n")

print("Log disimpan ke: results/log.txt")

# ====== GRAFIK VISUALISASI ======
labels = ['Thread 0', 'Thread 1']
x = range(len(labels))

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Perbandingan Simulasi Cache Dengan & Tanpa Koherensi")

# Cache Hits
axs[0, 0].bar(x, result_no_coherence['cache_hits'], label='Tanpa Koherensi', alpha=0.7)
axs[0, 0].bar(x, result_with_coherence['cache_hits'], label='Dengan Koherensi', alpha=0.7)
axs[0, 0].set_title("Cache Hits")
axs[0, 0].set_xticks(x)
axs[0, 0].set_xticklabels(labels)
axs[0, 0].legend()

# Akses Memori
axs[0, 1].bar(x, result_no_coherence['mem_access'], label='Tanpa Koherensi', alpha=0.7)
axs[0, 1].bar(x, result_with_coherence['mem_access'], label='Dengan Koherensi', alpha=0.7)
axs[0, 1].set_title("Akses Memori")
axs[0, 1].set_xticks(x)
axs[0, 1].set_xticklabels(labels)
axs[0, 1].legend()

# Pesan Koherensi
axs[1, 0].bar(['Koherensi'], [result_with_coherence['coherence_msgs']], color='orange')
axs[1, 0].set_title("Jumlah Pesan Koherensi")

# Waktu Eksekusi
axs[1, 1].bar(['Tanpa Koherensi', 'Dengan Koherensi'],
              [result_no_coherence['exec_time'], result_with_coherence['exec_time']],
              color=['green', 'red'])
axs[1, 1].set_title("Waktu Eksekusi (detik)")

plt.tight_layout()
plt.savefig('results/grafik_output.png')
plt.show()
print("Grafik disimpan ke: results/grafik_output.png")
