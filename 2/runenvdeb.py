import multiprocessing


def run_script(script_name):
    # Run the given script
    import subprocess
    subprocess.call(['python', script_name])


if __name__ == '__main__':


    # Start the second script in a new process
    p1 = multiprocessing.Process(target=run_script, args=('env.py',))
    p1.start()
    
    # Start the second script in a new process
    p2 = multiprocessing.Process(target=run_script, args=('dub.py',))
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()
