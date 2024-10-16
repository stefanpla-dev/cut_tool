import subprocess
import os
## imports subprocess module so subprocess.run can run cut.py and capture its output.
## imports os to create and remove the test file sample_test.tsv

def test_extract_second_field():
    sample_content = "f0\tf1\n0\t1\n5\t6\n10\t11\n15\t16\n20\t21\n"
    sample_file = "tests/sample_test.tsv"
    with open(sample_file, 'w') as file:
        file.write(sample_content)
    
    expected_output = "f1\n1\n6\n11\n16\n21\n"

    result = subprocess.run(
        ['python', 'src/cut.py', '-f', '2', sample_file],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True
    )

    os.remove(sample_file)

    assert result.stdout == expected_output
    assert result.stderr == ''
    assert result.returncode == 0

## As of writing the extract_field method in cut.py, this method tests whether the cut.py program does so correctly.
## Creates some sample content at a specific path/filename. Opens the sample file in write mode (creating it if it doesn't exist). 'with' ensures the file is closed after writing.
## subprocess.run(...) runs the command 'python src/cut.py -f 2 tests/sample_test.tsv' in a new process and captures its output and error messages. Runs cut.py and passes -f 2 (second field should be extracted) and the test file to process. stdout captures the standard output of the process, stderr captures the standard error output of the proess. text=True ensures captured output is returned as a string rather than bytes. result variable contains all of this.
## assertions check whether the actual standard output matches the expected output, that there were no error messages and that the return code is 0 (as opposed to 1) indicating that the process completed successfully.