const availableTools = {
    'header': 'Header',
    'image': 'imageTool',
};

function debounce(fn, delay = 500) {
    let timer;

    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        fn(...args);
      }, delay);
    };
}

const updateTarget = debounce(async (editor, targetElem) => {
    try {
        const data = await editor.save();
        targetElem.textContent = JSON.stringify(data);
    } catch(err) {
        console.error('Error when saving data:\n', err);
    }
})

function getEditorToolsConfig(name) {
    const toolsData = document.querySelector(`#editorTools_${name}`)?.textContent;
    const tools = toolsData ? JSON.parse(toolsData) : null;
    let toolsConfig = {};
    const selectedTools = Object.keys(availableTools).filter(toolName => {
        if (!Object.keys(tools).includes(toolName)) return false;
        if (!tools[toolName]) return false;
        return true;
    })
    selectedTools.forEach(toolName => {
        toolsConfig[toolName] = {
            class: window[availableTools[toolName]]
        }
    })
    // console.log("Tools: \n", tools);
    return toolsConfig;
}

function getEditorData(name) {
    const initData = document.querySelector(`#editorData_${name}`)?.textContent;
    const data = initData ? JSON.parse(JSON.parse(initData)) : {};
    return data;
}

document.addEventListener('DOMContentLoaded', function () {
    const editorElem = document.querySelector('#editorjs');
    if (!editorElem) return;
    const elemName = editorElem?.dataset?.editorName;
    const initData = getEditorData(elemName);
    const targetElem = document.querySelector(`[name="${editorElem?.dataset?.editorTarget}"]`);
    const toolsConfig = getEditorToolsConfig(elemName);
    const editor = new EditorJS({
        holder: editorElem,
        data: initData || {},
        onChange: () => {
            updateTarget(editor, targetElem);
        },
        tools: toolsConfig,
    });
}, false);