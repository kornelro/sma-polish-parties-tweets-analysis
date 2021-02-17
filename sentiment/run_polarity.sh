if [ $1 == "clear" ];
then
    docker container prune
    docker rmi sma2_sentiment
    docker build -t sma2_sentiment .
fi

docker run --mount type=bind,source=/home/kornel/Projects/SMA/assignment-2-kornelro/data/since_09_16,target=/home/data sma2_sentiment python3 polarity.py