from moviepy.editor import VideoFileClip


ORIGIN_VIDEO = 'input_images/Devil-Girl.mp4'


def create_a_gif():
    clip = VideoFileClip(ORIGIN_VIDEO)
    clip.write_gif(ORIGIN_VIDEO[:-4] + '.gif', fps=5)

    return None


if __name__ == '__main__':
    create_a_gif()
