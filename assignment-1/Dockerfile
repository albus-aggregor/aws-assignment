FROM node:20-alpine AS build

WORKDIR /app

COPY assignment-1/package*.json .

SHELL ["/bin/sh", "-c"]

RUN npm install

COPY assignment-1/. .

FROM node:20-alpine

WORKDIR /app

COPY --from=build /app .

EXPOSE 3000

CMD ["node", "app.js"]
