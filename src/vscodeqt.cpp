#include "vscodeqt.h"

vscodeqt::vscodeqt(QWidget* parent)
    : QMainWindow(parent)
    , ui(new Ui_vscodeqt)
{
    ui->setupUi(this);
}

vscodeqt::~vscodeqt()
{
    delete ui; 
}