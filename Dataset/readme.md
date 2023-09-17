# Dataset by Roboflow
# https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety

## 1.The dataset includes 2801 images. Construction are annotated in YOLOv8 format.
## 2.Preprocessing:
<ol>
  <li>Auto-orientation of pixel data (with EXIF-orientation stripping).</li>
  <li>Resize to 640x640 (Stretch).</li>
</ol>

## 3.Augmentation: Augmentation was applied to create 5 versions of each source image.
<ol>
  <li> 50% probability of horizontal flip.</li>
  <li>Randomly crop between 0 and 20 percent of the image.</li>
  <li>Random rotation of between -12 and +12 degrees.</li>
  <li> Random shear of between -2° to +2° horizontally and -2° to +2° vertically.</li>
  <li>Random brigthness adjustment of between -25 and +25 percent.</li>
  <li>Random exposure adjustment of between -20 and +20 percent.</li>
  <li>Random Gaussian blur of between 0 and 0.5 pixels.</li>
</ol>
