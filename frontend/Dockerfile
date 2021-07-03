FROM node:10

RUN mkdir /client
WORKDIR /client
ADD ./frontend/package*.json /client/
RUN npm install
ADD . /client/