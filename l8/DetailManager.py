

class DetailManager:
    def __init__(self, ctx, readManager):
        self.ctx = ctx
        self.readManager = readManager

    def __call__(self):
        details = self.readManager.reader.getDetails(self.ctx.contents.masterList.currentRow())
        self.ctx.contents.remoteHostDisplay.setText(str(details['remote IP']))
        self.ctx.contents.methodDisplay.setText(details['method'])
        palette = self.ctx.contents.statusCodeDisplay.palette()
        if details['code'] in range(200, 299):
            palette.setColor(self.ctx.contents.statusCodeDisplay.backgroundRole(), '#00FF00')
        elif details['code'] in range(400, 599):
            palette.setColor(self.ctx.contents.statusCodeDisplay.backgroundRole(), '#FF0000')
        self.ctx.contents.statusCodeDisplay.setAutoFillBackground(True)
        self.ctx.contents.statusCodeDisplay.setPalette(palette)
        self.ctx.contents.statusCodeDisplay.display(details['code'])
        self.ctx.contents.sizeDisplay.display(details['size'])
        self.ctx.contents.resourceDisplay.setText(details['URI'])
        self.ctx.contents.dateDisplay.setDate(details['timestamp'].date())
        self.ctx.contents.timeDisplay.setTime(details['timestamp'].time())
        self.ctx.contents.localHostDisplay.setText(str(details['local IP']))
        self.ctx.contents.hostnameDisplay.setText(details['hostname'])