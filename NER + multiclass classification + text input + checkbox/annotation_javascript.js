//********************************************
//****SETTING 1ST LABEL OF NER AS DEFAULT*****
//********************************************
let prevHash = null
document.addEventListener('prodigyupdate', v => {
    const { task } = event.detail
    // Select the label input for the given default label
    const defaultLabel = document.querySelector('input[value="Opinion/sentiment expression"]')
    if (task._task_hash !== prevHash) {  // the displayed task has changed
        defaultLabel.click()  // simulate click
        prevHash = task._task_hash
    }

})

//********************************
//****KEY BINDING FOR CHECKBOX****
//********************************
//if user clicks 'c' then it checks the checkbox
document.querySelector('#root').addEventListener('keyup', function(event) {
    if (event.keyCode === 67) {  // key code for character "c"
        document.getElementById("sarcasm").click();
    }
})