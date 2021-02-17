if [ $1 == "clear" ];
then
    docker container prune
    docker rmi sma2_scraper
    docker build -t sma2_scraper .
fi

docker run --mount type=bind,source=/home/kornel/Projects/SMA/assignment-2-kornelro/scraper/scrapped_data,target=/home/scrapped_data sma2_scraper python3 scraper.py