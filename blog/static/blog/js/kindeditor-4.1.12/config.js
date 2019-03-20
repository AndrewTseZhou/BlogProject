KindEditor.ready(function () {
    KindEditor.create('textarea[name=content]', {
        width: '800px',
        height: '200px',
        uploadJson: '/admin/upload/kindeditor',
    });
});
