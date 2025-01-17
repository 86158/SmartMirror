﻿
namespace MirrorInstallerSbos
{
    partial class InstallMirror
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.rtbxOutput = new System.Windows.Forms.RichTextBox();
            this.btnInstall = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.btnSelenium = new System.Windows.Forms.Button();
            this.cbxPython = new System.Windows.Forms.CheckBox();
            this.lblMadeby = new System.Windows.Forms.Label();
            this.btnInstallScreenshot = new System.Windows.Forms.Button();
            this.btnMover = new System.Windows.Forms.Button();
            this.btnMirrorMove = new System.Windows.Forms.Button();
            this.tmrDelay = new System.Windows.Forms.Timer(this.components);
            this.btnStartMirror = new System.Windows.Forms.Button();
            this.tmrAppTick = new System.Windows.Forms.Timer(this.components);
            this.btnPythonPath = new System.Windows.Forms.Button();
            this.lbl1 = new System.Windows.Forms.Label();
            this.lblCurrentPath = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            // 
            // rtbxOutput
            // 
            this.rtbxOutput.Location = new System.Drawing.Point(12, 109);
            this.rtbxOutput.Name = "rtbxOutput";
            this.rtbxOutput.Size = new System.Drawing.Size(775, 305);
            this.rtbxOutput.TabIndex = 0;
            this.rtbxOutput.Text = "";
            // 
            // btnInstall
            // 
            this.btnInstall.Location = new System.Drawing.Point(12, 12);
            this.btnInstall.Name = "btnInstall";
            this.btnInstall.Size = new System.Drawing.Size(127, 36);
            this.btnInstall.TabIndex = 1;
            this.btnInstall.Text = "Install Python";
            this.btnInstall.UseVisualStyleBackColor = true;
            this.btnInstall.Click += new System.EventHandler(this.btnInstall_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 93);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(42, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Output:";
            // 
            // btnSelenium
            // 
            this.btnSelenium.Enabled = false;
            this.btnSelenium.Location = new System.Drawing.Point(12, 54);
            this.btnSelenium.Name = "btnSelenium";
            this.btnSelenium.Size = new System.Drawing.Size(127, 36);
            this.btnSelenium.TabIndex = 3;
            this.btnSelenium.Text = "Install Selenium";
            this.btnSelenium.UseVisualStyleBackColor = true;
            this.btnSelenium.Click += new System.EventHandler(this.btnSelenium_Click);
            // 
            // cbxPython
            // 
            this.cbxPython.AutoSize = true;
            this.cbxPython.Location = new System.Drawing.Point(145, 12);
            this.cbxPython.Name = "cbxPython";
            this.cbxPython.Size = new System.Drawing.Size(108, 17);
            this.cbxPython.TabIndex = 4;
            this.cbxPython.Text = "Already installed?";
            this.cbxPython.UseVisualStyleBackColor = true;
            this.cbxPython.CheckedChanged += new System.EventHandler(this.cbxPython_CheckedChanged);
            // 
            // lblMadeby
            // 
            this.lblMadeby.AutoSize = true;
            this.lblMadeby.Location = new System.Drawing.Point(9, 428);
            this.lblMadeby.Name = "lblMadeby";
            this.lblMadeby.Size = new System.Drawing.Size(121, 13);
            this.lblMadeby.TabIndex = 5;
            this.lblMadeby.Text = "Made by: Steven Bosch";
            // 
            // btnInstallScreenshot
            // 
            this.btnInstallScreenshot.Enabled = false;
            this.btnInstallScreenshot.Location = new System.Drawing.Point(145, 54);
            this.btnInstallScreenshot.Name = "btnInstallScreenshot";
            this.btnInstallScreenshot.Size = new System.Drawing.Size(127, 36);
            this.btnInstallScreenshot.TabIndex = 6;
            this.btnInstallScreenshot.Text = "Install Selenium Screenshot";
            this.btnInstallScreenshot.UseVisualStyleBackColor = true;
            this.btnInstallScreenshot.Click += new System.EventHandler(this.btnInstallScreenshot_Click);
            // 
            // btnMover
            // 
            this.btnMover.Enabled = false;
            this.btnMover.Location = new System.Drawing.Point(278, 54);
            this.btnMover.Name = "btnMover";
            this.btnMover.Size = new System.Drawing.Size(127, 36);
            this.btnMover.TabIndex = 7;
            this.btnMover.Text = "Install webdriver";
            this.btnMover.UseVisualStyleBackColor = true;
            this.btnMover.Click += new System.EventHandler(this.btnMover_Click);
            // 
            // btnMirrorMove
            // 
            this.btnMirrorMove.Enabled = false;
            this.btnMirrorMove.Location = new System.Drawing.Point(411, 54);
            this.btnMirrorMove.Name = "btnMirrorMove";
            this.btnMirrorMove.Size = new System.Drawing.Size(127, 36);
            this.btnMirrorMove.TabIndex = 8;
            this.btnMirrorMove.Text = "Install the mirror";
            this.btnMirrorMove.UseVisualStyleBackColor = true;
            this.btnMirrorMove.Click += new System.EventHandler(this.btnMirrorMove_Click);
            // 
            // tmrDelay
            // 
            this.tmrDelay.Tick += new System.EventHandler(this.tmrDelay_Tick);
            // 
            // btnStartMirror
            // 
            this.btnStartMirror.Enabled = false;
            this.btnStartMirror.Location = new System.Drawing.Point(561, 54);
            this.btnStartMirror.Name = "btnStartMirror";
            this.btnStartMirror.Size = new System.Drawing.Size(201, 36);
            this.btnStartMirror.TabIndex = 9;
            this.btnStartMirror.Text = "Launch Mirror";
            this.btnStartMirror.UseVisualStyleBackColor = true;
            this.btnStartMirror.Click += new System.EventHandler(this.btnStartMirror_Click);
            // 
            // tmrAppTick
            // 
            this.tmrAppTick.Interval = 60;
            this.tmrAppTick.Tick += new System.EventHandler(this.tmrAppTick_Tick);
            // 
            // btnPythonPath
            // 
            this.btnPythonPath.Location = new System.Drawing.Point(352, 12);
            this.btnPythonPath.Name = "btnPythonPath";
            this.btnPythonPath.Size = new System.Drawing.Size(70, 23);
            this.btnPythonPath.TabIndex = 11;
            this.btnPythonPath.Text = "Select python3.9.exe";
            this.btnPythonPath.UseVisualStyleBackColor = true;
            this.btnPythonPath.Click += new System.EventHandler(this.btnPythonPath_Click);
            // 
            // lbl1
            // 
            this.lbl1.AutoSize = true;
            this.lbl1.Location = new System.Drawing.Point(259, 15);
            this.lbl1.Name = "lbl1";
            this.lbl1.Size = new System.Drawing.Size(87, 13);
            this.lbl1.TabIndex = 12;
            this.lbl1.Text = "Python.exe path:";
            // 
            // lblCurrentPath
            // 
            this.lblCurrentPath.AutoSize = true;
            this.lblCurrentPath.Location = new System.Drawing.Point(329, 38);
            this.lblCurrentPath.Name = "lblCurrentPath";
            this.lblCurrentPath.Size = new System.Drawing.Size(351, 13);
            this.lblCurrentPath.TabIndex = 13;
            this.lblCurrentPath.Text = "C:/Users/steve/AppData/Local/Microsoft/WindowsApps/python3.9.exe";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(258, 38);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(68, 13);
            this.label3.TabIndex = 15;
            this.label3.Text = "Current path:";
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // InstallMirror
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.lblCurrentPath);
            this.Controls.Add(this.lbl1);
            this.Controls.Add(this.btnPythonPath);
            this.Controls.Add(this.btnStartMirror);
            this.Controls.Add(this.btnMirrorMove);
            this.Controls.Add(this.btnMover);
            this.Controls.Add(this.btnInstallScreenshot);
            this.Controls.Add(this.lblMadeby);
            this.Controls.Add(this.cbxPython);
            this.Controls.Add(this.btnSelenium);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnInstall);
            this.Controls.Add(this.rtbxOutput);
            this.Name = "InstallMirror";
            this.Text = "Smartmirror";
            this.Load += new System.EventHandler(this.InstallMirror_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox rtbxOutput;
        private System.Windows.Forms.Button btnInstall;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnSelenium;
        private System.Windows.Forms.CheckBox cbxPython;
        private System.Windows.Forms.Label lblMadeby;
        private System.Windows.Forms.Button btnInstallScreenshot;
        private System.Windows.Forms.Button btnMover;
        private System.Windows.Forms.Button btnMirrorMove;
        private System.Windows.Forms.Timer tmrDelay;
        private System.Windows.Forms.Button btnStartMirror;
        private System.Windows.Forms.Timer tmrAppTick;
        private System.Windows.Forms.Button btnPythonPath;
        private System.Windows.Forms.Label lbl1;
        private System.Windows.Forms.Label lblCurrentPath;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
    }
}

