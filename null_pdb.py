import os
STRUCTURE= ['RS','TSA']

def create_pdb(structure,index,time,tp):

    #Make cpptraj input

    pdb = f"""

    parm /bp1/mulholland/zn22275/300K_MalL_{structure}/dry.MalL_{structure}.prmtop

    trajin /user/work/zn22275/null_{structure}/{index}/null_md{time}_dry.nc

    trajout /user/work/zn22275/{structure}_null_pdb/run_{index}/null_md{time}_{tp}.pdb onlyframes {tp} pdb

    go

"""    

# Write the file
    with open('pdb.in', "w") as f:
        f.write(pdb)
   
    # Execute cpptraj using os.system
    command = "cpptraj -i pdb.in"
    exit_code = os.system(command)


run=[1,2,3,4,5,6,7,8,9,10]
times = [i for i in range(100, 500, 20)]
timepoints = [2, 5, 7, 10, 12, 25, 50, 125, 150, 200, 250, 500, 750, 1000, 1250, 2500]
#apply function

for structure in STRUCTURE:

    for index in run:
        for time in times:
            for tp in timepoints:

                create_pdb(structure=structure,

                            index=str(index),

                            time=str(time),
                            
                            tp=str(tp))