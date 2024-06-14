#!/bin/bash




if [ -f ~/domain_pref.txt ]; then
	tasks_completed=(n n n n n n n n n)
	mentee_dom=()
	for d in sysad web app; do
		if [ -d ~/$d ]; then
			mentee_dom+=($d)
		fi
	done
	v=0
	for dom in ${mentee_dom[@]}; do
		for n in 1 2 3; do
			PS3="Is the task-$n for $dom is done?(for yes-enter 1, for no-enter 2): "
			select task_completed in y n; do
				if [[ $task_completed == "y" ]]; then
					if [ -d ~/$dom/task$n ]; then
						tasks_completed[$v]=$task_completed
					else
						mkdir ~/$dom/task$n
						chown $USER:${USER}_group ~/$dom/task$n
						chmod -R 770 ~/$dom/task$n
						tasks_completed[$v]=$task_completed
					fi
				else
					if [ -d ~/$dom/task$n ]; then
						rm -R ~/$dom/task$n
					fi
				fi
				v=$(($v+1))
				echo $task_completed
				break
			done

		done
	done
	v=0
	if [ -f ~/task_submitted.txt ]; then
		rm -R ~/task_submitted.txt
	fi
 	submittedTask=""
	for doma in Sysad Web App; do
		for nu in 1 2 3; do
   			submittedTask="${submittedTask}${tasks_completed[$v]"
			v=$(($v+1))
		done
	done
 	export submittedTask
 	python3 /scripts/submitted_task.py

elif [ -f ~/allocatedMentees.txt ]; then

	readarray -t allocated_mentees < <(awk '{print $2}' ~/allocatedMentees.txt)
	readarray -t domain_allocated_mentees < <(awk '{print $3}' ~/allocatedMentees.txt)
	if [ -s $(awk "NR==2 {print \$3}" ~/allocatedMentees.txt) ]; then
		line=2
	else
		line=1
	fi
	domain=$(awk "NR==$line {print \$3}" ~/allocatedMentees.txt)
	echo $domain
	for allocated_mentee in ${allocated_mentees[@]}; do
		task_completed=(n n n)
		for h in 1 2 3; do

			c=$(($h - 1))

			if [ -d $(eval echo ~$allocated_mentee)/$domain/task$h ]; then

				ln -s -f $(eval echo ~$allocated_mentee)/$domain/task$h ~/submittedTasks/task$h/$allocated_mentee
				echo "successfully created a symlink for task$h with the $allocated_mentee\'s task$h"

				if [ -z "$(ls -A $(eval echo ~$allocated_mentee)/$domain/task$h)" ]; then
					task_completed[$c]=n
				else
					task_completed[$c]=y
				fi
			fi
		done

		case $domain in
			"sysad") allocatedDomain=Sysad;;
			"web") allocatedDomain=Web;;
			"app") allocatedDomain=App;;
		esac
  		export allocatedDomain
  		completedTask=""
  		for i in ${task_completed[@]}; do
    			completedTask="${completedTask}${i}"
    		done
      		export completedTask
		export allocated_mentee
  		python3 /scripts/completed_task.py
	done
else
	echo "you are neither a mentee nor a mentor, and hence cannot run this command"

fi
