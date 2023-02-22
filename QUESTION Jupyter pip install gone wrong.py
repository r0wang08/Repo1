# not sure what happened. Just followinig teh pip install to install juypter notebook. I fist did pip
# I fist did "pip install jupyter" on VSC, then error message pasted below. Not sure what happened/
# then I did the following prompt: pip show jupyter
# next: setx PATH "the location c: of the location from pip show jupyter"
# i don't know what to do now.

tion.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-events.exe is installed in 'C:\Users\rongq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-console.exe is installed in 'C:\Users\rongq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-server.exe is installed in 'C:\Users\rongq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-nbclassic-bundlerextension.exe, jupyter-nbclassic-extension.exe, jupyter-nbclassic-serverextension.exe and jupyter-nbclassic.exe are installed in 'C:\Users\rongq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.   
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-bundlerextension.exe, jupyter-nbextension.exe, jupyter-notebook.exe and jupyter-serverextension.exe are installed in 'C:\Users\rongq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Send2Trash-1.8.0 anyio-3.6.2 argon2-cffi-21.3.0 argon2-cffi-bindings-21.2.0 arrow-1.2.3 asttokens-2.2.1 attrs-22.2.0 backcall-0.2.0 beautifulsoup4-4.11.2 bleach-6.0.0 cffi-1.15.1 colorama-0.4.6 comm-0.1.2 debugpy-1.6.6 decorator-5.1.1 defusedxml-0.7.1 executing-1.2.0 fastjsonschema-2.16.2 fqdn-1.5.1 ipykernel-6.21.2 ipython-8.10.0 ipython-genutils-0.2.0 ipywidgets-8.0.4 isoduration-20.11.0 jedi-0.18.2 jinja2-3.1.2 jsonpointer-2.3 jsonschema-4.17.3 jupyter-1.0.0 jupyter-client-8.0.3 jupyter-console-6.5.1 jupyter-core-5.2.0 jupyter-events-0.6.3 jupyter-server-2.3.0 jupyter-server-terminals-0.4.4 jupyterlab-pygments-0.2.2 jupyterlab-widgets-3.0.5 markupsafe-2.1.2 matplotlib-inline-0.1.6 mistune-2.0.5 nbclassic-0.5.2 nbclient-0.7.2 nbconvert-7.2.9 nbformat-5.7.3 nest-asyncio-1.5.6 notebook-6.5.2 notebook-shim-0.2.2 packaging-23.0 pandocfilters-1.5.0 parso-0.8.3 pickleshare-0.7.5 platformdirs-3.0.0 prometheus-client-0.16.0 prompt-toolkit-3.0.36 psutil-5.9.4 pure-eval-0.2.2 pycparser-2.21 pygments-2.14.0 pyrsistent-0.19.3 python-dateutil-2.8.2 python-json-logger-2.0.6 pywin32-305 pywinpty-2.0.10 pyyaml-6.0 pyzmq-25.0.0 qtconsole-5.4.0 qtpy-2.3.0 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 six-1.16.0 sniffio-1.3.0 soupsieve-2.4 stack-data-0.6.2 terminado-0.17.1 tinycss2-1.2.1 tornado-6.2 traitlets-5.9.0 uri-template-1.2.0 wcwidth-0.2.6 webcolors-1.12 webencodings-0.5.1 websocket-client-1.5.1 widgetsnbextension-4.0.5

[notice] A new release of pip available: 22.3.1 -> 23.0
[notice] To update, run: C:\Users\rongq\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS C:\Users\rongq\Repositories\Repo1> pip show jupyter
Name: jupyter
p0\localcache\local-packages\python310\site-packages
Requires: ipykernel, ipywidgets, jupyter-console, nbconvert, notebook, qtconsole
Required-by:
PS C:\Users\rongq\Repositories\Repo1> setx PATH p0\localcache\local-packages\python310\site-packages                                            Requires: ipykernel, ipywidgets, jupyter-console, nbconvert, notebook, qtconsole                Required-by:                                    PS C:\Users\rongq\Repositories\Repo1> setx PATH "^C
PS C:\Users\rongq\Repositories\Repo1> setx PATH "Location: c:\users\rongq\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages"

SUCCESS: Specified value was saved.
PS C:\Users\rongq\Repositories\Repo1>