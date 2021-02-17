if [ $1 == "clear" ];
then
    docker container prune
    docker rmi sma2_vis
    docker build -t sma2_vis .
fi

docker run -p 8888:8888 \
--mount type=bind,source=/home/kornel/Projects/SMA/assignment-2-kornelro/visualisation/notebooks,target=/home/work \
--mount type=bind,source=/home/kornel/Projects/SMA/assignment-2-kornelro/data/since_09_16,target=/home/data \
sma2_vis jupyter-notebook --notebook-dir="./home/work" --ip=0.0.0.0 --allow-root --NotebookApp.token='abc'