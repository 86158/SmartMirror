
namespace MirrorInstallerSbos
{
    partial class Launch
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
            this.btnLaunchMirror = new System.Windows.Forms.Button();
            this.rtbxCmdOutput = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // btnLaunchMirror
            // 
            this.btnLaunchMirror.Location = new System.Drawing.Point(12, 12);
            this.btnLaunchMirror.Name = "btnLaunchMirror";
            this.btnLaunchMirror.Size = new System.Drawing.Size(354, 47);
            this.btnLaunchMirror.TabIndex = 1;
            this.btnLaunchMirror.Text = "Launch Mirror";
            this.btnLaunchMirror.UseVisualStyleBackColor = true;
            this.btnLaunchMirror.Click += new System.EventHandler(this.btnLaunchMirror_Click);
            // 
            // rtbxCmdOutput
            // 
            this.rtbxCmdOutput.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.rtbxCmdOutput.Location = new System.Drawing.Point(12, 65);
            this.rtbxCmdOutput.Name = "rtbxCmdOutput";
            this.rtbxCmdOutput.Size = new System.Drawing.Size(354, 233);
            this.rtbxCmdOutput.TabIndex = 2;
            this.rtbxCmdOutput.Text = "";
            // 
            // Launch
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.ClientSize = new System.Drawing.Size(382, 309);
            this.Controls.Add(this.rtbxCmdOutput);
            this.Controls.Add(this.btnLaunchMirror);
            this.Name = "Launch";
            this.Text = "Launch";
            this.TransparencyKey = System.Drawing.Color.Gray;
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnLaunchMirror;
        private System.Windows.Forms.RichTextBox rtbxCmdOutput;
    }
}