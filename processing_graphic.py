import re
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Función para parsear el log y extraer la información necesaria
def parse_log(log_file):
    # Patrón para extraer la marca de tiempo y el mensaje del log que contiene el tiempo total de procesamiento
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) INFO Processed in ([\d\.]+) seconds order ([\w-]+)')
    data = []
    
    with open(log_file, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                timestamp_str = match.group(1)
                process_time_str = match.group(2)
                order_id = match.group(3)
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
                process_time = float(process_time_str)
                data.append((timestamp, order_id, process_time))
    
    return data

# Función para graficar los tiempos de procesamiento
def plot_processing_times(data):
    timestamps = [item[0] for item in data]
    processing_times = [item[2] for item in data]
    
    # Calcular métricas
    mean_time = np.mean(processing_times)
    std_dev_time = np.std(processing_times)
    median_time = np.median(processing_times)

    # Graficar los tiempos de procesamiento
    plt.figure(figsize=(14, 7))
    plt.plot(timestamps, processing_times, marker='o', label='Processing Time')
    
    # Agregar líneas de métricas
    plt.axhline(y=mean_time, color='r', linestyle='-', label=f'Mean: {mean_time:.2f} s')
    plt.axhline(y=median_time, color='g', linestyle='-', label=f'Median: {median_time:.2f} s')
    plt.axhline(y=mean_time + std_dev_time, color='b', linestyle='--', label=f'Std Dev: +{std_dev_time:.2f} s')
    plt.axhline(y=mean_time - std_dev_time, color='b', linestyle='--')

    plt.xlabel('Timestamp')
    plt.ylabel('Processing Time (seconds)')
    plt.title('Processing Time Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Imprimir métricas en la consola
    print(f'Mean Processing Time: {mean_time:.2f} seconds')
    print(f'Standard Deviation of Processing Time: {std_dev_time:.2f} seconds')
    print(f'Median Processing Time: {median_time:.2f} seconds')

# Archivo de logs
log_file = 'processing_service.log'  # Reemplazar con la ruta al archivo de logs

# Parsear el log y extraer los datos
data = parse_log(log_file)

# Graficar los tiempos de procesamiento
plot_processing_times(data)
