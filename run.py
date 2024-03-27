import subprocess

subprocess.run(["D:\\APPS\\AnaConda\\envs\\anaconda\\python", "test_on_video.py",
                "--dataset_path", "../../0Dataset/UCF101/UCF-101",
                "--video_path", "../../0Dataset/UCF101/UCF-101/Basketball/v_Basketball_g01_c01.avi",
                "--checkpoint_model", "model_checkpoints/ConvLSTM_150.pth"])
