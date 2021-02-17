if [ $1 == "clear" ];
then
    docker container prune
    docker rmi sma2_app
    docker build -t sma2_app .
fi

docker run sma2_app