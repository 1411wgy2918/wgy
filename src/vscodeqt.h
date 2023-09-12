#pragma once
#include "ui_vscodeqt.h"
#include <QMainWindow>

class vscodeqt : public QMainWindow {
    Q_OBJECT
    
public:
    vscodeqt(QWidget* parent = nullptr);
    ~vscodeqt();

private:
    Ui_vscodeqt* ui;
};