docker compose down

docker rmi panda
docker rmi cookies
docker rmi login
docker rmi home
docker rmi userdb

cd ctf1

docker build -t panda .

cd ..

cd ctf2

docker build -t cookies .

cd ..

cd ctf3

docker build -t login .

cd ..

cd website

docker build -t home .

cd ..

cd mysqls

docker build -t userdb .

cd ..

docker compose up -d

