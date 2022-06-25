function deleteNote(noteId) {
    console.log("🚀 ~ file: index.js ~ line 2 ~ deleteNote ~ noteId", noteId)
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href = "/"
    })
}