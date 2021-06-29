using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;




namespace MirrorInstallerSbos
{
    public partial class InstallMirror : Form
    {
        public InstallMirror()
        {
            InitializeComponent();
        }
        static string PATH = Application.StartupPath + "\\..\\..\\";
        static string Program;
        string TextOutput;
        int delay;
        string result;
        bool newLine = false;
        private void btnInstall_Click(object sender, EventArgs e)
        {
            Program = "python-3.9.5-amd64.exe";
            OpenProgram();
            rtbxOutput.AppendText("Launched: " + PATH + Program);
            rtbxOutput.AppendText("\nEnabled the Selenium install button\n");
            btnSelenium.Enabled = true;
            btnInstallScreenshot.Enabled = true;
            btnMover.Enabled = true;
            btnMirrorMove.Enabled = true;
        }
        private void cbxPython_CheckedChanged(object sender, EventArgs e)
        {
            if (cbxPython.Checked == true)
            {
                btnSelenium.Enabled = true;
                btnInstallScreenshot.Enabled = true;
                btnMover.Enabled = true;
                btnMirrorMove.Enabled = true;
                rtbxOutput.AppendText("Enabled the Selenium install button\n\n");
            }
        }


        static void OpenProgram()
        {
            Process myProcess = new Process();

            try
            {
                myProcess.StartInfo.UseShellExecute = false;
                // You can start any process, HelloWorld is a do-nothing example.
                myProcess.StartInfo.FileName = PATH + Program;
                myProcess.StartInfo.CreateNoWindow = false;
                myProcess.Start();
                // This code assumes the process you are starting will terminate itself.
                // Given that is is started without a window so you cannot terminate it
                // on the desktop, it must terminate itself or you can do it programmatically
                // from this application using the Kill method.
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        private void btnSelenium_Click(object sender, EventArgs e)
        {
            Process cmd = new Process();
            cmd.StartInfo.FileName = "cmd.exe";
            cmd.StartInfo.RedirectStandardInput = true;
            cmd.StartInfo.RedirectStandardOutput = true;
            cmd.StartInfo.CreateNoWindow = false;
            cmd.StartInfo.UseShellExecute = false;
            cmd.Start();

            cmd.StandardInput.WriteLine("pip install Selenium");
            cmd.StandardInput.Flush();
            cmd.StandardInput.WriteLine("y");
            cmd.StandardInput.Close();
            cmd.WaitForExit();
            rtbxOutput.AppendText(cmd.StandardOutput.ReadToEnd() + "\n");
        }

        private void btnInstallScreenshot_Click(object sender, EventArgs e)
        {
            Process cmd = new Process();
            cmd.StartInfo.FileName = "cmd.exe";
            cmd.StartInfo.RedirectStandardInput = true;
            cmd.StartInfo.RedirectStandardOutput = true;
            cmd.StartInfo.CreateNoWindow = false;
            cmd.StartInfo.UseShellExecute = false;
            cmd.Start();

            cmd.StandardInput.WriteLine("pip install Selenium-Screenshot");
            cmd.StandardInput.Flush();
            cmd.StandardInput.WriteLine("y");
            cmd.StandardInput.Close();
            cmd.WaitForExit();
            rtbxOutput.AppendText(cmd.StandardOutput.ReadToEnd() + "\n");
        }

        private void btnMover_Click(object sender, EventArgs e)
        {
            string path = PATH + "Chromedriver.exe";
            string path2 = "C:\\Program Files (x86)\\Chromedriver.exe";
            try
            {
                if (!File.Exists(path))
                {
                    // This statement ensures that the file is created,
                    // but the handle is not kept.
                    using (FileStream fs = File.Create(path)) { }
                }

                // Ensure that the target does not exist.
                if (File.Exists(path2))
                    File.Delete(path2);

                // Move the file.
                File.Copy(path, path2);
                Console.WriteLine("{0} was moved to {1}.", path, path2);

                // See if the original exists now.
                if (File.Exists(path))
                {
                    Console.WriteLine("The original file still exists, which is unexpected.");
                    TextOutput = "Chromedriver is moved to " + path2 + " \nThe original file still exists, which is unexpected.";
                }
                else
                {
                    Console.WriteLine("The original file no longer exists, which is expected.");
                    TextOutput = "Chromedriver is moved to " + path2 + "\nThe original file no longer exists, which is expected.";
                }
            }
            catch 
            {
                Console.WriteLine("The process failed: {0}", e.ToString());
            }
            rtbxOutput.AppendText(TextOutput + "\n");
        }

        private void btnMirrorMove_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Make sure you have Winrar installed in C:/Program Files/WinRAR/");
            //moved the chromedriver now the smartmirror itself

            rtbxOutput.AppendText("Moving the mirror to the right place");

            string path1 = PATH + "SmartMirror.rar";
            string path21 = "C:\\Smartmirror.rar";
            try
            {
                if (!File.Exists(path1))
                {
                    // This statement ensures that the file is created,
                    // but the handle is not kept.
                    using (FileStream fs = File.Create(path1)) { }
                }

                // Ensure that the target does not exist.
                if (File.Exists(path21))
                    File.Delete(path21);

                // Move the file.
                File.Copy(path1, path21);
                Console.WriteLine("{0} was moved to {1}.", path1, path21);

                // See if the original exists now.
                if (File.Exists(path1))
                {
                    Console.WriteLine("The original file still exists, which is unexpected.");
                    TextOutput = "Smartmirror is moved to " + path21 + " \nThe original file still exists, which is unexpected.\n";
                }
                else
                {
                    Console.WriteLine("The original file no longer exists, which is expected.");
                    TextOutput = "Smartmirror is moved to " + path21 + "\nThe original file no longer exists, which is expected.\n";
                }
                tmrDelay.Start();

            }
            catch
            {
                Console.WriteLine("The process failed: {0}", e.ToString());
            }

        }

        private void tmrDelay_Tick(object sender, EventArgs e)
        {
            delay++;
            if (delay == 20)
            {
                tmrDelay.Stop();
                const string source = "C:\\Smartmirror.rar";
                string destinationFolder = source.Remove(source.LastIndexOf('.'));
                System.Diagnostics.Process p = new System.Diagnostics.Process();
                p.StartInfo.CreateNoWindow = true;
                p.StartInfo.UseShellExecute = false;
                p.StartInfo.FileName = "\"C:\\Program Files\\WinRAR\\winrar.exe\"";
                p.StartInfo.Arguments = string.Format(@"x -s ""{0}"" *.* ""{1}\""", source, destinationFolder);
                p.Start();
                p.WaitForExit();
                delay = 0;
                tmrDelay.Stop();
            }
            if (newLine == true)
            {
                rtbxOutput.AppendText(result + "\n");
                newLine = false;
            }
        }

        private void btnStartMirror_Click(object sender, EventArgs e)
        {
            run_cmd("C:/Users/steve/AppData/Local/Microsoft/WindowsApps/python3.9.exe", "C:/Smartmirror/www/eduarte.py");

        }
        private void run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = cmd;//cmd is full path to python.exe
            start.Arguments = args;//args is path to .py file and any cmd line args
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            start.CreateNoWindow = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    result = reader.ReadLine();
                    newLine = true;
                    Console.Write(result);
                }
            }
        }
    }
}

