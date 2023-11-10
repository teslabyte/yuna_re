//var native = Module.getBaseAddress("libur.so");

function hook_first_xor(){
    var offset = '0xd2facc'

    var first_xor_address = native
    first_xor_address = first_xor_address.add(offset)

    Interceptor.attach(first_xor_address ,{
        onEnter: function(args){
            
            var buffer_size = args[1].toInt32();
            var key_index = args[2].toInt32();

            var out_string = "First xor use (ENCRYPT) :\n"+"\tBuffer size="+buffer_size+"\n\tKey index ="+key_index+"\n"
            console.log(out_string)

            var buffer = args[0].readByteArray(buffer_size)
            //console.log(hexdump(buffer))
            
        }, onLeave: function(retval){
        }
    })
}

function hook_write(){
    var offset = "0xd2fb50";

    var write_address = native
    write_address = write_address.add(offset)

    Interceptor.attach(write_address,{
        onEnter: function(args){
            var first_arg = args[0]
            var buffer_size = args[2].toInt32()
            var buffer = args[1].readByteArray(buffer_size)

            console.log("WRITE BUFFER SIZE=" + buffer_size)
            send(Array.from(new Uint8Array(buffer)));
        }, onLeave: function(retval){

        }
    })
}

function hook_second_xor(){
    var offset = '0xd2fc2c'

    var second_xor_address = native
    second_xor_address = second_xor_address.add(offset)

    Interceptor.attach(second_xor_address ,{
        onEnter: function(args){
            
            
            var buffer_size = args[1].toInt32();
            var key_index = args[2].toInt32();
            var t = args[0].readByteArray(buffer_size)

            var out_string = "Second xor use :\n"+"\tBuffer size="+buffer_size+"\n\tKey index ="+key_index+"\n"
            console.log(out_string)
            
        }, onLeave: function(retval){
        }
    })
}

function hook_third_xor(){
    var offset = '0xd2fd28'

    var third_xor_address = native
    third_xor_address = third_xor_address.add(offset)

    Interceptor.attach(third_xor_address ,{
        onEnter: function(args){
            
            var buffer_size = args[1].toInt32();
            var key_index = args[2].toInt32();

            var out_string = "Third xor use :\n"+"\tBuffer size="+buffer_size+"\n\tKey index ="+key_index+"\n"
            //console.log(out_string)

            var buffer = args[0].readByteArray(buffer_size);
            //console.log(hexdump(buffer))
            //send({ data: Array.from(new Uint8Array(buffer)), index: key_index});
            
        }, onLeave: function(retval){
        }
    })

}

function hook_lz4_uncompress(){
    var offset = '0xd2fe80'
    
    var lz4_uncompress_address = native
    lz4_uncompress_address = lz4_uncompress_address.add(offset)

    Interceptor.attach(lz4_uncompress_address, {
        onEnter: function(args){
            var buffer_third = args[0]
            var v38 = args[1]
            var v55 = args[2]
            var v56_minus_v55 = args[3]
            var v45 = args[4]

            var out_string = "LZ4_UNCOMPRESS\n\tBuffer_third=" + buffer_third + "\n\tv38=" + v38 + "\n\tv55=" + v55 + "\n\tv56-v55=" + v56_minus_v55 + "\n\tv45=" + v45
            console.log(out_string)
        }
    })
}

function hook_lbnum(){
    //var offset = '0xcf2238'
    var offset = '0x1349738'

    var pigz_address = native
    pigz_address = pigz_address.add(offset)

    Interceptor.attach(pigz_address,{
        onEnter: function(args){
            
        }, onLeave: function(retval){
            console.log("SIZE:", retval.toInt32())
        }
    })
}

function hook_gcs(){
    var rhcore_module = Process.findModuleByName("librhcore.so")
    var rhcore = rhcore_module.base
    var offset = '0xed29c'

    var fun_address = rhcore.add(offset)

    Interceptor.attach(fun_address, {
        onEnter: function(args){
            var a1 = args[0]
            console.log("GCS: a1 = ", a1)
        }, onLeave: function(retval){
            console.log("GCS: Return value=", retval)
        }
    })
}

function curl(){
    var rhcore_module = Process.findModuleByName("librhcore.so")
    var rhcore = rhcore_module.base
    //var offset = '0x2aa6ac'
    var offset = '0xf05d0'

    var fun_address = rhcore.add(offset)

    Interceptor.attach(fun_address, {
        onEnter: function(args){
            
            var a1 = args[0].readCString()
            var a2 = args[1].readCString()
            var a3 = args[2].readCString()

            console.log("a1=",a1)
            console.log("a2=",a2) 
            console.log("a3=",a3) 
            
        }, onLeave: function(retval){
            console.log("Return value=", retval)
        }
    })
}

//var timeout = setTimeout(hook_func_name, 500);

var t = setTimeout(hook_gcs, 500)
var t1 = setTimeout(curl, 500)
