# 1. Helmet-and-Vest-detection-using-Yolov8
~Author : Pratham Sanshi🤗

![image_55_jpg rf 27ae4341a9b9647d73a8929ff7a22369](https://github.com/Prathama-sanshi/Helmet-and-Vest-detection-using-Yolov8/assets/59955378/a1b334fe-1603-4da3-ab55-76581ff536c2)


<hr>

# 2. Steps to run the model:
<ol>
  
<li>
<p>Create a new folder (lets say helmet_vest)in your desktop and open command prompt in that folder itself.
  Virtualenv is a tool to set up your Python environments.To install virtualenv copy the command and past it in your cmd.
</p>
  
```bash
pip install virtualenv
```
  This will install the Virtualenv tool.
</li>
<li>
  
  Now we create a new virtual environment named 'myenv_for_ultralytics'. 
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
  Once the dependencies are installed, we activate the environment that we have created.
    
```bash
 env/Scripts/activate.bat
```
</li>
<li>
  To make sure the dependencies are installed we list the requirments.If the we see list of python libraries, then we have successfully installed all requirments.
  
  ```bash
 pip list
```
</li>
<li>
Copy Test_yolo_model.py and save it in the folder(helmet_vest) that we have created in the beginning. Now download the best.pt model and save it in same folder.Now copy the path best.pt and past it inside Test_yolo_model.py. We are ready to run the code .Past the following code and you will get a popup asking for webcam ,allow and the model will start classifyting image.To quit form algorithm press 'q'.
  
  ```bash
python Test_yolo_model.py
```

</li>
  <li>
    Lastely to deactivate the environment we use this command.
    
  ```bash
~deactivate
```
  </li>
</ol>

## 3. Why do we need virtual environment?
<p>
  The very basic approach to run a python program is to install all the dependencies or libraries via the terminal. Write all the code in one .py file and run the program. This is most common approach performed by every novice. This works great for the small python projects then , why do we need an environment? To answer this lets understand a scenario.
</p>
<p>
  You are working on some project_A and you installed all the libraries, lets just say X_library_version_1.0 to your global python library. Now you switch to project_B which also requires libraries but different version , lets just say X_library_version_2.8. Now you execute the project_B successfully, but again if you try to execute project_A then you will face errors on dependencies/libraries. The only way to solve the issue is to create a seperate virtual environment for each project so that the dependencies do not alter. 
</p>

# 4. Flow Diagram

![image](https://github.com/Prathama-sanshi/Helmet-and-Vest-detection-using-Yolov8/assets/59955378/9efccf93-9d8b-45b8-a21b-41e9ed05d420)



###### Resources :
###### For more information on Ultralytics check: https://github.com/ultralytics/ultralytics/blob/main/README.md
###### Dataset link : https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety

