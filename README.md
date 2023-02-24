****
MONGO

Instância MongoDB
IP: 192.168.50.155
Porta: 27017
usuário: usuario1
senha: mongodbmongodb

Obs: para adicionar outros IPs à máquina, ver o tutorial "Permitir conexões externas no MongoDB"

****
LINUX

** Configurações da máquina virtual
- Mudar rede de "NAT" para "Bridged Adapter"
- Como foi criado um disco virtual extra, e é nele que são instalados os arquivos do banco de dados [1][2], o disco não está como auto-montado, nem os containers no Docker estão como "Restat Always", logo é necessário

1) Entrar no programa Discos, do CentOS, e montar o arquivo com o disco virtual. Ele deve montar em /dev/sda
2) Iniciar os serviços do Docker e verificar se ele vai apontar para o local certo

[1] /run/media/<user>/mongodisk/mongodb
[2] /run/media/<user>/mongodisk/postgresql

** Configurar IP estático no CentOS
> Ir em configurações > Rede

** Instalar o MongoDB no CentOS
https://hostadvice.com/how-to/how-to-install-mongodb-on-centos/

** Criar usuário e alterar configurações do MongoDB
https://gist.github.com/royz/46397fe4ee25dc14418b41821ee45335

** Permitir conexões externas no Mongodb
https://www.digitalocean.com/community/tutorials/how-to-configure-remote-access-for-mongodb-on-centos-8



** Portainer **
url: http://192.168.50.155:9000
usuário: admin
senha: linuxlinuxlinux

** Incluir autenticação no Mongodb dentro do Portainer
https://betterprogramming.pub/add-authentication-to-mongodb-in-portainer-docker-30a60ab7858a

****
DOCKER

https://www.mongodb.com/compatibility/deploying-a-mongodb-cluster-with-docker


** Criar instância do MongoDB, com o volume criado no disco virtual anexado
docker run -d -p 27017:27017 --name mongo1 --network mongoCluster --restart no -v /run/media/<user>/mongodisk/mongodb/data1:/data/db mongo:6 mongod --replSet myReplicaSet --bind_ip localhost,mongo1

docker run -d -p 27018:27017 --name mongo2 --network mongoCluster --restart no -v /run/media//<user>/mongodisk/mongodb/data2:/data/db mongo:6 mongod --replSet myReplicaSet --bind_ip localhost,mongo2

docker run -d -p 27019:27017 --name mongo3 --network mongoCluster --restart no -v /run/media//<user>/mongodisk/mongodb/data3:/data/db mongo:6 mongod --replSet myReplicaSet --bind_ip localhost,mongo3

** Rodar esse comando para dizer ao Mongo para ser em ReplicaSet
docker exec -it mongo1 mongosh --eval "rs.initiate({_id: \"myReplicaSet\", members: [{_id: 0, host: \"mongo1\"},{_id: 1, host: \"mongo2\"},{_id: 2, host: \"mongo3\"}]})"

** String de conexão com o banco (usar no Mongo Compass)
mongodb://mongo1:27017,mongo2:27018,mongo3:27019/?replicaSet=myReplicaSet


****
Host

*Adicionar o IP e o nome das instância do Mongo em /etc/hosts
mongo1 192.168.50.155
mongo2 192.168.50.155
mongo3 192.168.50.155


****
PostgreSQL

1) Foi criado por meio de arquivo docker-compose.yml, que está dentro de /home//<user>/postgresql/docker-compose.yml

2) Utilizado este guia

https://github.com/lebarreiroj/postgreSQL_PGAdmin4

3) Acesso pelo endereço: http://192.168.50.155:16543/ (pgAdmin)
usuário: <e-mail>
senha: postgresql

** Inclusão de servidor do PostgreSQL no pgAdmin
usuário: postgresql
senha: postgresql

