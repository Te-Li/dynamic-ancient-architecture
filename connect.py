from PIL import Image, ImageSequence

def combine_gifs(gif_paths, output_path):
    # 打开第一个 GIF，获取其帧序列
    with Image.open(gif_paths[0]) as im:
        frames = [frame.copy() for frame in ImageSequence.Iterator(im)]

    # 遍历后续的 GIF 文件
    for path in gif_paths[1:]:
        with Image.open(path) as im:
            # 将当前 GIF 的帧序列追加到总帧序列中
            frames.extend([frame.copy() for frame in ImageSequence.Iterator(im)])

    # 保存合并后的 GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=im.info['duration'], loop=0)

# 示例用法
gif_paths = ['2.gif', '4.gif','5.gif']  # 替换为你的 GIF 文件路径
output_path = 'combined.gif'  # 输出文件路径
combine_gifs(gif_paths, output_path)