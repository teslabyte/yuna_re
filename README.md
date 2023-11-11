# yuna_re
Collection of scripts i used to reverse engineer API of a certain game made in Yuna engine

- Intercepting loadbufferx and loadbuffer and exporting decrypted Lua files  
- Hooking the main encryption method yuna_xor and replicated it in python  
- Replicated AES256-CBC that the game uses to encrypt certain config files  
- Replicated functions var_45_4() and var_45_5() from Lua files that are used with request authentication  
- hook.js is used for hooking any other function i thought looked interesting  

# Notes:   
- Most of the games encryption and authentication logic is inside the libur.so shared library and Lua (luajit compiled bytecode) files    
- The game uses a mix of HTTP requests and TCP messages for communicating with the server
- If you want Lua files, don't bother with loadbuffer, just hook loadbufferx  
