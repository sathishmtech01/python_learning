#list of images
image_list = ["Alpha001.png","Alpha002.png","Alpha003.png","Alpha004.png"]
iteration=10
#output path
output_path="output/list_{}.ifl"
for i in range(0,iteration):
    # output path with file
    file=output_path.format(i)
    out = "\n".join(image_list)
    with open(file,"w") as f:
        f.write(out)
    image_list = image_list[1:] + image_list[:1]
    print(out)
