import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
logger = modbus_tk.utils.create_logger("console")

'''execute(slave, function_code, starting_address, quantity_of_x=0, output_value=0, data_format="", 
expected_length=-1, write_starting_address_FC23=0) '''

# 连接MODBUS TCP从机
master = modbus_tcp.TcpMaster(host="127.0.0.1")
master.set_timeout(5.0)
logger.info("connected")

# 读保持寄存器
demo1 = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 9)
print(demo1)
# 读输入寄存器
logger.info(master.execute(3, cst.READ_INPUT_REGISTERS, 0, 9, output_value=1))