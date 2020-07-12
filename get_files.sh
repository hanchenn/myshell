#!/bin/bash

#遍历一个文件夹
function across_files()
{
	echo "-------------Dir $1----------------"
	cd $1
	files=$(ls $1)
	for file in ${files}
	do
		#输出文件名
		echo ${file}
		#修改后缀名	
		mv ${file} $(echo ${file} | cut -d '.' -f 1).log	
	done
	return 0
}

#function change_filenames(){}

function prepare()
{

	#创建一个文件夹，用来存放待批处理的文件
	mkdir files_to_be_solved
	#创建一堆空文件
	cd files_to_be_solved
	for ((i=0;i<10;i++))
	do
		touch ${i}_file.txt
	done
}

across_files $1

