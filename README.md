# Helmet-and-Vest-detection-using-Yolov8

![image_55_jpg rf 27ae4341a9b9647d73a8929ff7a22369](https://github.com/Prathama-sanshi/Helmet-and-Vest-detection-using-Yolov8/assets/59955378/510616bd-2b96-41f4-aef4-0d352eb94ea6)

# Steps to rum model:
<ol>
  
<li>
<p>Create a new folder (lets say helmet_vest)in your desktop and open command prompt in that folder itself.
  Now to create a virtual environment we need tool .Virtualenv is a tool to set up your Python environments.
</p>
  
```bash
pip install virtualenv
```
  This will install the Virtualenv tool.
</li>
<li>
  
  Now we create a new virtual environment named 'myenv'. 
  ```bash
python3 -m venv myenv_for_ultralytics
``` 
</li>
<li>
  We install all the requirments for ultralytics by using this command.
  
```bash
pip install ultralytics
```
</li>
<li>
  Once the dependencies are installed we activate the environment that we have created.
    
```bash
 env/Scripts/activate.bat //In CMD
```
</li>
<li>
  TO make sure the dependencies are installed we list the requirments.If the we see list of python libraries then we have successfully installed all requirments.
  
  ```bash
 pip list
```
</li>
<li>
Copy this Test_yolo_model.py and save it in the folder that we have created in the beggining

</li>
  
  

</ol>




#### For more information on Ultralytics : https://github.com/ultralytics/ultralytics/blob/main/README.md
#### you can find the requirments.txt in their github repo be sure to check
