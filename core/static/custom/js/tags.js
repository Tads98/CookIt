const tagContainer = document.querySelector(".tag-container");
const input = document.querySelector(".tag-container input");
var tags = [];

function createTag(label) {
    const div = document.createElement('div');
    div.setAttribute('class', 'tag btn-primary rounded-pill');
    const span = document.createElement('span');
    span.innerHTML = label;
    span.setAttribute('class', 'mr-1');
    const close = document.createElement('i');
    close.setAttribute('class', 'fas fa-times');
    close.setAttribute('data-item', label);
    div.appendChild(span);
    div.appendChild(close);
    const input = document.createElement('input');
    input.setAttribute('type', 'hidden');
    input.setAttribute('value', label);
    input.setAttribute('name', 'ingredientes');
    div.appendChild(input);
    return div;
}

function resetTags() {
    document.querySelectorAll('.tag').forEach(function (tag) {
        tag.parentElement.removeChild(tag);
    })
}

function addTags() {
    resetTags();
    tags.slice().reverse().forEach(function (tag) {
        const input = createTag(tag);
        tagContainer.prepend(input);
    })
}

input.addEventListener('keyup', function addTag(e) {
    if (e.code == 'Space') {
        str = input.value.slice(0, -1);
        console.log(str);
        tags.push(str);
        addTags();
        input.value = '';
    }
});

/*TODO: adicionar função de remoção de tag remoção de tag */