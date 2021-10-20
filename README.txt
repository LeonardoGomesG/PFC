Égide
Projeto para o monitoramente de desfigurações de urls dentro de um determinado domínio.

Preparação
Usando Pyhton 3.7

O projeto se utiliza da tecnologia Tesseract da google. Para instalação, deve-se seguir as seguintes instruções:

Tesseract_Windows;
Tesseract_Linux;
A seguir, deve-se fazer a intalação das dependencias com

pip install -r requirements.txt
Configuração
Configurações de execução do processo a serem configuradas no arquivo do setup/config.py:

recursive.base: Urls pelas quais irão se começar a busca recursiva.

recursive.domain: Lista de domínios aos quais serão restritas, respectivamente, a busca iniciada pelas urls na base.

recursive.max_depth: Número que limita a profundidade da recursão. Utilizado em testes para ver o inicio e o fim do processo. Caso não configurado, ou configurado como None, não haverá limite, e será percorrido todos sítios válidos contidos no domínio.

max_threads: Número que limita a quantidade máxima de threads que vão estar em execução simultaneamente.

load_previous_data: Booleano True/False. Decide se utiliza o arquivo data.json previamente carregado ou analisa todos os domínios novamente.

rerun_recursion: Booleano True/False. Decide se o módulo recursivo será executado novamente ou apenas a detecção e classificação baseadas nos dados salvos em data.json.

tesseract_path: Caminho para o executável do programa Tesseract necessário para o módulo de classificação.

notification.from_email: Endereço de email do qual será enviado o alerta.

notification.password: Senha para apps gerada para o email do qual será enviado o alerta.

notification.to_email: Endereço de email para o qual será enviado o alerta.

Execução
Execução do programa é a partir do arquivo main.py após a configurações:

python3 ./main.py