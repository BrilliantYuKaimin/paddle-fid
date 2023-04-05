# 用飞桨计算 FID 分数

这是一个用飞桨计算[弗雷歇 Inception 距离](https://arxiv.org/abs/1706.08500)（FID）的仓库，迁移它的 [PyTorch 实现](https://github.com/mseitzer/pytorch-fid)和 [PaddleGAN](https://github.com/PaddlePaddle/PaddleGAN) 中的[实现](https://github.com/PaddlePaddle/PaddleGAN/blob/develop/ppgan/metrics/fid.py)。

## 安装

先克隆本仓库，再使用 pip 安装：
```bash
git clone https://github.com/BrilliantYuKaimin/paddle-fid
pip install -e paddle-fid
```

## 使用

运行下面的命令可以计算两个目录中的图片间的 FID：

```bash
python -m paddle_fid 图片目录甲 图片目录乙
```

如果安装了 GPU 版本的飞桨却想使用 CPU 进行推理，可以添加选项 `--device cpu`。
