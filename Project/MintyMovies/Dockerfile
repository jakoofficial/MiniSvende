FROM node:20-bullseye-slim

WORKDIR /app

COPY package*.json ./
RUN npm install --omit=dev

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["node", "build/index.js", "--host", "0.0.0.0"]