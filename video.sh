#!/usr/bin/env bash
ffmpeg -framerate 30 -start_number 0 -i Move-img-Loop/img/image-%05d.png -r 30 -an -vcodec libx264 -pix_fmt yuv420p Move-img-Loop/out1.mp4
