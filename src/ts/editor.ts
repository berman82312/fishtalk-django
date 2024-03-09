import EditorJS from '@editorjs/editorjs';
import Header from '@editorjs/header';
// import ImageTool from '@editorjs/image';

function debounce(fn: Function, delay = 500) {
    let timer: number;

    return (...args: any) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        fn(...args);
      }, delay);
    };
}

const updateTarget = debounce(async (editor: EditorJS, targetElem: HTMLTextAreaElement) => {
    try {
        const data = await editor.save();
        targetElem.textContent = JSON.stringify(data);
    } catch(err) {
        console.error('Error when saving data:\n', err);
    }
})

document.addEventListener('DOMContentLoaded', function () {
    const editorElem = document.querySelector<HTMLDivElement>('#editorjs');
    if (!editorElem) return;
    const initData = editorElem?.dataset?.editorData ? JSON.parse(editorElem?.dataset?.editorData) : {};
    const targetElem = document.querySelector(`[name="${editorElem?.dataset?.editorTarget}"]`)
    const editor = new EditorJS({
        holder: editorElem,
        data: initData || {},
        onChange: () => {
            updateTarget(editor, targetElem);
        },
        tools: {
            header: Header,
        }
    });
}, false);
