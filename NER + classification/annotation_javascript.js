//********************************************
//****SETTING 1ST LABEL OF NER AS DEFAULT*****
//********************************************
let prevHash = null
document.addEventListener('prodigyupdate', event => {
    const { task } = event.detail
    // Select the label input for the given default label
    const defaultLabel = document.querySelector('input[value="Weather"]')
    if (task._task_hash !== prevHash) {  // the displayed task has changed
        defaultLabel.click()  // simulate click
        prevHash = task._task_hash
    }

})

