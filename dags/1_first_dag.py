from airflow.sdk import dag, task



@dag(
    dag_id = "first_dag",
)

def first_dag():
    
    
    @task.python
    def first_task():
        print("This is forst task")
        
    @task.python
    def second_task():
        print("This is sec task")
        
    @task.python
    def third_task():
        print("This is third task")
    
    
    first=first_dag()
    second=second_task()
    third=third_task()
    
    first >> second >> third
   
# Instantiating the DAG
first_dag()
