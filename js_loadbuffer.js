function hook_native(){
    var native = Module.getBaseAddress("libur.so");
    //console.log("Base add : " + native);

    var offset = '0xe31c70'; //luaL_loadbufferx
    //var offset = '0xe31db8' //luaL_loadstring
    //var offset = '0xe31a6c' //luaL_loadfilex
    //var offset = '0x761e40' //send !!!
    //var offset = '0xde2ab0' //yuna::net::socket::write
    //var offset = '0x763504';


    native = native.add(offset);
    //console.log("Func add : " + native);

    Interceptor.attach(native ,{
        onEnter: function(args){
            var len = args[2].toInt32(); // length of the file
            var code = args[1].readByteArray(len);//readCString(len); // content
            
            //console.log(str)
            //const a3 = args[2].readCString();
            //console.log(`a3: ${a3}`);
            //console.log("ARG :", args[1]);
            
            //console.log("ARG :", args[2]);
            //Use with Python script:
            send({ path: args[3].readCString() /* filename */, dump: Array.from(new Uint8Array(code)) });

            // Write to file from console output with > output.txt
            //if(args[3].readCString() == "17") console.log(code);
        }, onLeave: function(retval){
            //console.log("Return value: ", retval);
        }
    })
}

var timeout = setTimeout(hook_native, 500);

