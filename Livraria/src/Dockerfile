# Usar imagem oficial do Node.js
FROM node:18

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY package.json package-lock.json ./
RUN npm install

# Copiar o restante dos arquivos
COPY . .

# Expor a porta da API
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["node", "src/server.js"]
