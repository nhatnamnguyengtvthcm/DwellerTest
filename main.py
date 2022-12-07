# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from services import  create_connect_jdbc, excute_model
import jpype
# jar = r'/opt/drivers/fmjdbc.jar'
# args='-Djava.class.path=%s' % jar
# jvm_path = jpype.getDefaultJVMPath()
# jpype.startJVM(jvm_path, args)
from xml.dom import minidom, getDOMImplementation
import os
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create connection with Database through JDBC
    curs = create_connect_jdbc()
    # create model
    excute_model(curs)
    # print(results)
    # curs.execute(
    #     ("""
    #         SELECT it.table_name, ic.column_name, ic.data_type, isc.CONSTRAINT_NAME FROM information_schema.tables as it  left join information_schema.columns as ic
    #         ON  it.table_name = ic.table_name left join information_schema.constraint_column_usage isc on
    #          ic.column_name = isc.column_name WHERE it.table_schema = 'public'
    #      """))
    curs.execute(
        """
            SELECT table_name from information_schema.tables WHERE table_schema = 'public'


        """
    )
    tables = curs.fetchall()
    tables_list = [item[0] for item in tables]

    curs.execute(
        """
            select cl.column_name, cl.data_type, ccu.CONSTRAINT_NAME from information_schema.columns cl left join information_schema.constraint_column_usage ccu on cl.column_name = ccu.column_name where cl.table_name = 'roles' ;


        """
    )

    meta_data_roles = curs.fetchall()

    meta_data_roles = [list(item) for item in meta_data_roles]
    print(meta_data_roles)

    # export meta for Roles Users
    curs.execute(
        """
            select cl.column_name, cl.data_type, ccu.CONSTRAINT_NAME from information_schema.columns cl left join information_schema.constraint_column_usage ccu on cl.column_name = ccu.column_name  where cl.table_name = 'users' ;
        """
    )
    meta_data_users = curs.fetchall()
    meta_data_users = [list(item) for item in meta_data_users]
    print(meta_data_users)
    impl = getDOMImplementation()
    root = impl.createDocument(None, "root", None)
    # root = minidom.Document()
    roles_xml = root.createElement('generate')
    root.firstChild.appendChild(roles_xml)
    # root.appendChild(roles_xml)
    roles_primary_key = None
    for idx in range(len(meta_data_roles)):
        if meta_data_roles[idx][0] != roles_primary_key:
            pass
        if 'roles_pkey' in meta_data_roles[idx]:
            child = root.createElement("id")
            child.setAttribute('type', meta_data_roles[idx][1])
            roles_xml.appendChild(child)
            primary_key = meta_data_roles[idx][0]

        elif meta_data_roles[idx][2] == None:
            child = root.createElement("attribute")
            child.setAttribute('name', meta_data_roles[idx][0])
            child.setAttribute('type', meta_data_roles[idx][1])
            roles_xml.appendChild(child)

    # root = minidom.Document()
    users_xml = root.createElement('generate')
    # root.appendChild(users_xml)
    root.firstChild.appendChild(users_xml)
    users_primary_key = None
    for idx in range(len(meta_data_users)):
        if meta_data_users[idx][0] != users_primary_key:
            pass
        if 'users_pkey' in meta_data_users[idx]:
            child = root.createElement("id")
            child.setAttribute('type', meta_data_users[idx][1])
            users_primary_key = meta_data_users[idx][0]
            users_xml.appendChild(child)
        elif meta_data_users[idx][2] != None:
            if 'fk_' in meta_data_users[idx][2]:
                child = root.createElement("reference")
                child.setAttribute('name', meta_data_users[idx][0])
                child.setAttribute('type', meta_data_users[idx][1])
                users_xml.appendChild(child)
        elif meta_data_users[idx][2] == None:
            child = root.createElement("attribute")
            child.setAttribute('name', meta_data_users[idx][0])
            child.setAttribute('type', meta_data_users[idx][1])
            users_xml.appendChild(child)

    xml_str = root.toprettyxml(indent = "\t")
    save_path_file = "test.xml"
    with open(save_path_file, "w") as f:
        f.write(xml_str)

