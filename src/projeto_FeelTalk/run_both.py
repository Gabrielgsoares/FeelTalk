import multiprocessing
import subprocess
import os
import sys

# Obtendo o caminho para o interpretador Python
python_executable = sys.executable

# Defindo o caminho para os scripts
path_to_main = os.path.join(os.path.dirname(__file__), 'main.py')
path_to_tracking = os.path.join(os.path.dirname(__file__), 'tracking.py')

#Função para executar um script
def run_script(script_path):
    subprocess.run([python_executable, script_path])

if __name__ == '__main__':
    # Criando processos para ambos os scripts
    process_main = multiprocessing.Process(target=run_script, args=(path_to_main,))
    process_tracking = multiprocessing.Process(target=run_script, args=(path_to_tracking,))

    # Iniciando os processos
    process_main.start()
    process_tracking.start()

    #Aguardando os processos ficarem prontos processos
    process_main.join()
    process_tracking.join()
