tasks=(wikihow toolbench toolalpaca lumos alfworld webshop os)
# tasks=(seal_tools)
model_name="gpt-3.5-turbo"
for task in ${tasks[@]}; do
    python node_eval.py \
        --task gen_workflow \
        --model_name ${model_name} \
        --gold_path ./gold_traj/${task}/graph_eval.json \
        --pred_path ./pred_traj/${task}/${model_name}/graph_eval_two_shot.json\
        --task_type ${task} \
        --few_shot \

done