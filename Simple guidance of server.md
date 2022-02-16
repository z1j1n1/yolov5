Simple guidance of the speed test in repo YOLOv5

+ 查看显卡占用

```buildoutcfg
$ nvidia-smi

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.57       Driver Version: 450.57       CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:1A:00.0 Off |                  N/A |
| 27%   35C    P0    51W / 250W |      0MiB / 11019MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  GeForce RTX 208...  Off  | 00000000:1B:00.0 Off |                  N/A |
| 28%   40C    P0    63W / 250W |      0MiB / 11019MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   2  GeForce RTX 208...  Off  | 00000000:1C:00.0 Off |                  N/A |
| 27%   38C    P0    51W / 250W |      0MiB / 11019MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   3  GeForce RTX 208...  Off  | 00000000:1D:00.0 Off |                  N/A |
| 28%   39C    P0    74W / 250W |      0MiB / 11019MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```

选定你需要使用的卡（比如卡$0,3$)
官方的README中，Yolo-v5的训练脚本为：

```bash
python train.py --data coco.yaml --cfg yolov5n.yaml --weights '' --batch-size 128
                                       yolov5s                                64
                                       yolov5m                                40
                                       yolov5l                                24
                                       yolov5x                                16
```

你需要在这条命令前面加上 `CUDA_VISIBLE_DEVICES=xxxx`，指定使用的显卡，比如：
```bash
CUDA_VISIBLE_DEVICES=0,3 python train.py --data coco.yaml --cfg yolov5n.yaml --weights '' --batch-size 128
```
这时就会用4张卡来训练你的模型
建议：训练用4卡，测速用单卡

训练建议开一个`tmux`窗口来做，这样你断开服务器之后进程不会自己结束，可以过一天再去看训练结果如何，`tmux`用法可以上网查，类似于开个后台

+ Docker

启动：

```bash
sudo docker run --ipc=host -it ultralytics/yolov5:latest
```

这个是yolov5的镜像，里面有他们的源代码，但是没有数据，需要数据的话可以挂载一个文件夹到docker上，例如：

```bash
sudo docker run --gpus all --ipc=host -v "$(pwd)"/dataset_path:/usr/src/dataset -it ultralytics/yolov5:latest
```

类似的，你的新的yaml和代码可以通过这种方式，放到一个文件夹中挂载到docker中

进入docker之后其实你可以认为就是一个小的虚拟机，其他命令都是用linux的命令就可以了。

+ Misc
训练在25服务器上跑，测速在29服务器上用docker跑