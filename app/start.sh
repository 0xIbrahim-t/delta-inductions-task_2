#!/bin/bash



script_files=(check_deregistered.sh completed_task.py starting.sh custom_conf.sh submitted_task.py cronjob.sh deRegister.sh delete_noti.sh displayStatus.sh domainPref.sh mentorAllocation.sh notification.sh setQuiz.sh submitTask.sh userGen.sh answerQuiz.sh)
for script_file in ${script_files[@]}; do
	chmod -R 755 /scripts/$script_file
done

alias_script_files=(deRegister.sh displayStatus.sh domainPref.sh mentorAllocation.sh setQuiz.sh submitTask.sh userGen.sh answerQuiz.sh)
for alias_script_file in ${alias_script_files[@]}; do
	echo "alias ${alias_script_file:0:-3}='/scripts/$alias_script_file'" >> ~/.bashrc
done
