# Vue 3 + Vite
# Tailwindcss
# Aplicação de reservas de estações de trabalho
- Projeto criado com o intuito de resolver o problema que as empresas estão enfrentando depois do Covid19,
com o aumento de colaboradores trabalhando de forma remota, após a pandemia as empresas necessitam que os colaboradores voltem trabalhar presencialmente de forma hibrida.
Porém o espaço da empresa não suporta todos os colaboradores presencialmente.Pensando nesse problema foi criado uma aplicação que o usuário realiza a reserva do dia e horário que deseja ir trabalhar presencialmente,
assim evitando a super lotação da empresa.
# Instruções para rodar projeto.
- O frontend foi construído com os Frameworks Vuejs 3 e Vite
- Certifique-se que tenha o Node instalado em sua máquina, rode no terminal (node -v) caso nao tenha instalado será precisa fazer o download nesse link(https://nodejs.org/en).
- Depois de feito o download é só seguir a instalação, basicamente será next next.
- Certifique-se que tenha o vue instalado em sua máquina.
- Rode o npm install, isso irá ler o arquivo package.json e instalar as dependências.
- Em seguida rode o comando npm run dev, com isso o servidor será inicializado, 
- Só copiar e colar a url no navegador ou segurar o CRTL e clicar no link que gerou no terminal.
- Será preciso criar salas pelo Django admin.
- O campo sala no formulário criar reserva é preciso passar um number ( número criado pelo django admin ao criar salas ou número da sala exibido na tela do frontend ao lado do formulário.
# PONTO DE ATENÇÃO
- Ao término do projeto me deparei com bugs na renderização da lista de estações de trabalho, onde ao atualizar a página
 os dados da lista de estações não é carregada por algum motivo, fiz vários testes não encontrando o problema por hora!
 - PORÉM A FORMA DE VISUALIZAR A LISTA CASO NÃO RENDERIZE, será alterar as linhas 
 {{ item.id }}{{ item.name }} do código frontend linha 59 e 60
 basicamente seria retirar .name de item.name e salvar e depois dar CTRL Z até voltar para item.name!
 # Link para o Figma contendo prints da tela e comentários sobre o fluxo da aplicação.
 - https://www.figma.com/file/DHPFkixhvLSdSG0hcTVHkw/Untitled?type=design&t=R83HnJwdhUsUHeqi-1
# Capturas da tela

# Tela Inicial

![image](https://github.com/jeferson1985/station_reservation/assets/58534889/c836271d-a502-4eab-8155-0909da3767d4)
# Tela Mapa
![image](https://github.com/jeferson1985/station_reservation/assets/58534889/2ed2e87f-884d-4806-a506-f192eb227586)
# Tela Lista de Reservas
![image](https://github.com/jeferson1985/station_reservation/assets/58534889/926a1114-48f1-4169-a71c-4029397a1e66)
# Tela Fazer Reserva
![image](https://github.com/jeferson1985/station_reservation/assets/58534889/f6cc19d3-38d5-44aa-aa28-a8e1c671424b)


