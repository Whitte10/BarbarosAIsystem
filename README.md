
# Barbaros USV obstacle detection and avoidance algorithm

This algorithm is an algorithm that detects obstacles via yolov5 in line with the barbaros usv system autonomous obstacle avoidance algorithm. It gives the following outputs according to the position of the obstacle over the safe zone it has drawn.

## Run it on your computer

download the project

```bash
  https://github.com/Whitte10/BarbarosAIsystem
```

go to project path

```bash
  cd my-project
```

install required packages

```bash
  pip install /r requirements.txt
```

run the code

```bash
  python3 detect.py 
```
Note:if you are in ubuntu specify main folder location on line 8
  
## Specifications

- Ubuntu support (change on line 8 required)
- Windows support
- Compatibility with different inputs (by inserting images into testimages)
- Compatibility with different resolutions

  
## Associated Projects

Here are some related projects

[YoloV5](https://github.com/ultralytics)

  
## Technologies Used

**İslemci:** Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz   2.59 GHz

**GPU:** Nvidia RTX2060

  
## Lessons Learned

In the test images, the horizon line and the ship lines are sometimes confused because the POV images also include parts of the ship where the camera is mounted. In order to solve this error, the edges detected at the bottom of the picture were not included in the calculation and the horizon line was tried to be calculated in this way.
And our model need more training because sometimes it can not detect obstacles accordingly
  
## Screenshot
Ros detection
![Uygulama Ekran Görüntüsü](https://user-images.githubusercontent.com/109946449/211011800-1ff9c623-3764-4527-bb50-fdb0241bd032.jpeg)


Real World Dtection
![Uygulama Ekran Görüntüsü](https://user-images.githubusercontent.com/85283487/211012392-0808f0b1-7fc8-497f-9e45-c8d30200532a.png)
  
## Authors and Acknowledgments

- [@Whitte10](https://www.github.com/Whitte10) for design and development.
- [@scbektas](https://www.github.com/scbektas) for design and testing.
- [@berkanyasar](https://www.github.com/berkanyasar) for testing.

  
## Feedback

If you have any feedback, please contact us at barbarosida53@gmail.com.
  
## Support

Email barbarosida53@gmail.com for support.

  